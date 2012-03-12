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

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

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
		String		fileNameIn	= "R_3-15_src.txt";	/* src file: contains a text	*/
		String		fileNameOut	= "R_3-15_out.txt";	/* replaced text 				*/
		
		/* modify fileName		*/
		fileNameIn					= String.format(
				"%s/%s", 
				new R_3_15_replace_all_matches_p205().
					getClass().getPackage().getName(),
				fileNameIn);
		fileNameOut					= String.format(
				"%s/%s", 
				new R_3_15_replace_all_matches_p205().
					getClass().getPackage().getName(),
				fileNameOut);
		
		/* get a BufferedWriter/Reader instance		*/
		BufferedReader	br				= STDLIB.getBufferedReader(fileNameIn);
		BufferedWriter	bw				= STDLIB.getBufferedWriter(fileNameOut);
		
		/* set up regex				*/
		Pattern		regex				= Pattern.compile("cat");	/* regex patter		*/
//		Matcher	regexMatcher	= regex.matcher(br.read());	/* matched object	*/		
		Matcher	regexMatcher	= regex.matcher(STDLIB.readAllContent(br));	/* matched object	*/
		
		/* write to file					*/
		try {
			bw.write(regexMatcher.replaceAll("<cat>"));
		} catch (IOException e1) {
			// TODO 自動生成された catch ブロック
			e1.printStackTrace();
			System.exit(1);
		}
		
		/* close streams			*/
		try {
			br.close();
		} catch (IOException e) {
			// TODO 自動生成された catch ブロック
			e.printStackTrace();
		}
		try {
			bw.close();
		} catch (IOException e) {
			// TODO 自動生成された catch ブロック
			e.printStackTrace();
		}
		
		//debug
//		try {
////			System.out.println(Class.forName("R_3_15_replace_all_matches_p205").toString());
////			System.out.println("done");
////			Class.forName("R_3_15_replace_all_matches_p205").newInstance().
//		} catch (ClassNotFoundException e) {
//			// TODO 自動生成された catch ブロック
//			e.printStackTrace();
//		} finally {
//			System.exit(0);
//		}
		
		/* processes			*/
		
		
//		if (br != null) {
//			System.out.println("return=" + STDLIB.getFileWriter(fileName).toString());
//		} else {
//			System.out.println("return=null");
//		}//if (br != null)		
		
		
	}//public static void main(String[] args)

	public static void showMessage() {
		System.out.println("Hi.");
	}//public String elemType showMessage( paramName)
	
}
