/************************************`
 * STDLIB.java
 * Author: iwabuchiken
 * Date: 2012/2012/03/12/9:44:35
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
package mylib;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

/**
 * @author iwabuchiken
 *
 */
public class STDLIB {
	/**********************************************
	 * <name> getFileWriter
	 *  <description> generate a FileWriter instance
	 *  <parameter> 
	 *  	fileName:String
	 * <Return value>
	 * 		fr:FileWriter
	 **********************************************/
	public static FileWriter getFileWriter(String fileName) {
		/* variables			*/
		try {
			FileWriter		fr	= new FileWriter(new File(fileName));
			return fr;
		} catch (IOException e) {
			// TODO é©ìÆê∂ê¨Ç≥ÇÍÇΩ catch ÉuÉçÉbÉN
			e.printStackTrace();
			return null;
		}//try
	}//public static FileWriter getFileWriter(String fileName)
}
