/************************************`
 * R_3_20_split_HTML_tag.java
 * Author: iwabuchiken
 * Date: 2012/2012/03/15/7:44:14
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

import java.util.regex.Pattern;
import java.util.regex.PatternSyntaxException;

/**
 * @author iwabuchiken
 *
 */
public class R_3_20_split_HTML_tag {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ
		/* regex				*/
		RegEx.doRegex();
		
	}

}

class RegEx {
	public static void doRegex() {
		/* vars				*/
		String		targetString	= "I like <b>bold</b> and <i>italic</i> fonts";
		String[]		splitArray		= null;
		
		/* get the patter		*/
		try {
			Pattern regex = Pattern.compile("<[^<>]*>");
			splitArray = regex.split(targetString);
		} catch (PatternSyntaxException e) {
			// TODO: handle exception
			e.printStackTrace();
			System.exit(1);
		}
		
		/* display result			*/
		for (String item : splitArray) {
			System.out.print(item);
		}//for (String item : splitArray)
		System.out.println("\n");
	}//public void elemType doRegex()
}//class RegEx
