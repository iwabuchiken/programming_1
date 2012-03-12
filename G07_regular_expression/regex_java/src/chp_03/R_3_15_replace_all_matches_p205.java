/************************************`
 * R_3_15_replace_all_matches_p205.java
 * Author: iwabuchiken
 * Date: 2012/2012/03/12/9:08:52
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
package chp_03;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

import mylib.STDLIB;



/**
 * @author iwabuchiken
 *
 */
public class R_3_15_replace_all_matches_p205 {

	/**
	 * @param args
	 */
	public static void replace_all(String subjectString) {
		String		resultString	= subjectString.replaceAll("cat", "dog");
	}//public static void replace_all(String subjectString)
	
//	public static FileWriter getFileWriter(String fileName) {
//		/* variables			*/
//		try {
//			FileWriter		fr	= new FileWriter(new File(fileName));
//			return fr;
//		} catch (IOException e) {
//			// TODO 自動生成された catch ブロック
//			e.printStackTrace();
//			return null;
//		}//try
//	}//public static FileWriter getFileWriter(String fileName)
	
	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ
		/* variables			*/
		String		fileName	= "abc";
		/* modify fileName		*/
		fileName					= String.format(
				"%s/%s", 
				new R_3_15_replace_all_matches_p205().
					getClass().getPackage().getName(),
				fileName);
		
		FileWriter	fr				= STDLIB.getFileWriter(fileName);
		
		/* processes			*/
		if (fr != null) {
			System.out.println("return=" + STDLIB.getFileWriter(fileName).toString());
		} else {
			System.out.println("return=null");
		}//if (fr != null)		
	}//public static void main(String[] args)

}
