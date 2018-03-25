class testArray
{
	public static void main(String[] args) {
		System.out.println("hello testArray..");

		int a[]={45,8,8,7,90};
		try
		{
			System.out.print(a);
		}
		catch (Exception e) {
			e.printStackTrace();
		}
		// System.out.printf("%d\n",a);
		int sum=0;
		for (int i=0;i<5 ;i++ ) {
			// System.out.printf("a[%d]=%d\n",i,a[i]);
			sum=sum+a[i];
		}
		System.out.printf("sum=%d\n",sum);
	}
}