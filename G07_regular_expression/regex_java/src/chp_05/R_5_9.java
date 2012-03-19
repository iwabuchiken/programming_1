/************************************`
 * R_5_9.java
 * Author: iwabuchiken
 * Date: 2012/2012/03/13/8:27:21
 * Aim:								*
 * 	1.
 * <Usage>
 *	1. Run the program
 * <Source>
 * 	1. 
 ************************************/
/**
 * 
 */
package chp_05;

//import chp_03.R_5_9;

/**
 * @author iwabuchiken
 *
 */
public class R_5_9 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ
		/* vars			*/
		String		fileNameIn	= "R_5-9_src.txt";	/* src file: contains a text	*/
		String		fileNameOut	= "R_5-9_out.txt";	/* replaced text 				*/
		
		/* modify fileName		*/
		fileNameIn					= modifyFileName(fileNameIn);
//		fileNameIn					= String.format(
//				"%s/%s", 
//				new R_5_9().
//					getClass().getPackage().getName(),
//				fileNameIn);
		fileNameOut					= modifyFileName(fileNameOut);
//		fileNameOut					= String.format(
//				"%s/%s", 
//				new R_5_9().
//					getClass().getPackage().getName(),
//				fileNameOut);
		
	}//public static void main(String[] args)

	public static String modifyFileName(String fileName) {
		return String.format(
				"%s/%s", 
				new R_5_9().
					getClass().getPackage().getName(),
					fileName);
	}//public String elemType modifyFileName(String file_name)
}
