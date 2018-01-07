    import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
 
public class LocalSetup {
 
    private FileSystem fileSystem;
    private Configuration config;
 
     
    public LocalSetup() throws Exception {
        config = new Configuration();
 
         
        config.set("fs.file.impl", "org.apache.hadoop.fs.LocalFileSystem");
 
        fileSystem = FileSystem.get(config);
        if (fileSystem.getConf() == null) {
                throw new Exception("LocalFileSystem configuration is null");
        }
    }
 
     
    public Configuration getConf() {
        return config;
    }
 
     
    public FileSystem getLocalFileSystem() {
        return fileSystem;
    }
}

//In the next course of action we will setup a class which will read from the .tar.gz,.tgz,.tar.bz2 extension files and write it to the Sequence File with key as the name of file and value be the content of the file:

	
import org.apache.tools.bzip2.CBZip2InputStream;
import org.apache.tools.tar.TarEntry;
import org.apache.tools.tar.TarInputStream;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.LocalFileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.BytesWritable;
import org.apache.hadoop.io.SequenceFile;
import org.apache.hadoop.io.Text;
 
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.io.IOException;
import java.util.zip.GZIPInputStream;
 
 
 
public class TarToSeqFile {
 
    private File inputFile;
    private File outputFile;
    private LocalSetup setup;
 
     
    public TarToSeqFile() throws Exception {
        setup = new LocalSetup();
    }
 
     
    public void setInput(File inputFile) {
        this.inputFile = inputFile;
    }
 
    public void setOutput(File outputFile) {
        this.outputFile = outputFile;
    }
 
    public void execute() throws Exception {
        TarInputStream input = null;
        SequenceFile.Writer output = null;
        try {
            input = openInputFile();
            output = openOutputFile();
            TarEntry entry;
            while ((entry = input.getNextEntry()) != null) {
                if (entry.isDirectory()) { continue; }
                String filename = entry.getName();
                byte[] data = TarToSeqFile.getBytes(input, entry.getSize());
                 
                Text key = new Text(filename);
                BytesWritable value = new BytesWritable(data);
                output.append(key, value);
            }
        } finally {
            if (input != null) { input.close(); }
            if (output != null) { output.close(); }
        }
    }
 
    private TarInputStream openInputFile() throws Exception {
        InputStream fileStream = new FileInputStream(inputFile);
        String name = inputFile.getName();
        InputStream theStream = null;
        if (name.endsWith(".tar.gz") || name.endsWith(".tgz")) {
            theStream = new GZIPInputStream(fileStream);
        } else if (name.endsWith(".tar.bz2") || name.endsWith(".tbz2")) {
            fileStream.skip(2);
            theStream = new CBZip2InputStream(fileStream);
        } else {
            theStream = fileStream;
        }
        return new TarInputStream(theStream);
    }
 
    private SequenceFile.Writer openOutputFile() throws Exception {
        Path outputPath = new Path(outputFile.getAbsolutePath());
        return SequenceFile.createWriter(setup.getLocalFileSystem(), setup.getConf(),
                                         outputPath,
                                         Text.class, BytesWritable.class,
                                         SequenceFile.CompressionType.BLOCK);
    }
 
     
    private static byte[] getBytes(TarInputStream input, long size) throws Exception {
        if (size > Integer.MAX_VALUE) {
            throw new Exception("A file in the tar archive is too large.");
        }
        int length = (int)size;
        byte[] bytes = new byte[length];
 
        int offset = 0;
        int numRead = 0;
 
        while (offset < bytes.length &&
               (numRead = input.read(bytes, offset, bytes.length - offset)) >= 0) {
            offset += numRead;
        }
 
        if (offset < bytes.length) {
            throw new IOException("A file in the tar archive could not be completely read.");
        }
 
        return bytes;
    }
 
     
    public static void main(String[] args) {
        if (args.length != 2) {
            exitWithHelp();
        }
 
        try {
            TarToSeqFile me = new TarToSeqFile();
            me.setInput(new File(args[0]));
            me.setOutput(new File(args[1]));
            me.execute();
        } catch (Exception e) { 
            e.printStackTrace();
            exitWithHelp();
        }
    }
 
    public static void exitWithHelp() {
        System.err.println("Usage:  <tarfile> TarToSeqFile  <output>\n\n" +
                           "<tarfile> may be GZIP or BZIP2 compressed, must have a\n" +
                           "recognizable extension .tar, .tar.gz, .tgz, .tar.bz2, or .tbz2.");
        System.exit(1);
    }
}