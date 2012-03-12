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

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
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
			// TODO 自動生成された catch ブロック
			e.printStackTrace();
			return null;
		}//try
	}//public static FileWriter getFileWriter(String fileName)
	
	/**********************************************
	 * <name> getFileReader
	 *  <description> generate a FileReader instance
	 *  <parameter> 
	 *  	fileName:String
	 * <Return value>
	 * 		fr:FileReader
	 **********************************************/	
	public static FileReader getFileReader(String fileName) {
		/* variables			*/
		try {
			FileReader		fr	= new FileReader(new File(fileName));
			return fr;
		} catch (IOException e) {
			// TODO 自動生成された catch ブロック
			e.printStackTrace();
			return null;
		}//try
	}//public static FileReader getFileReader(String fileName)

	/**********************************************
	 * <name> getBufferedWriter
	 *  <description> generate a BufferedWriter instance
	 *  <parameter> 
	 *  	fileName:String
	 * <Return value>
	 * 		fr:BufferedWriter
	 **********************************************/
	public static BufferedWriter getBufferedWriter(String fileName) {
		/* variables			*/
		try {
			BufferedWriter		br	= new BufferedWriter(new FileWriter(new File(fileName)));
			return br;
		} catch (IOException e) {
			// TODO 自動生成された catch ブロック
			e.printStackTrace();
			return null;
		}//try
	}//public static BufferedWriter getFileWriter(String fileName)
	
	/**********************************************
	 * <name> getBufferedReader
	 *  <description> generate a BufferedReader instance
	 *  <parameter> 
	 *  	fileName:String
	 * <Return value>
	 * 		fr:BufferedReader
	 **********************************************/
	public static BufferedReader getBufferedReader(String fileName) {
		/* variables			*/
		try {
			BufferedReader		fr	= new BufferedReader(new FileReader(new File(fileName)));
			return fr;
		} catch (IOException e) {
			// TODO 自動生成された catch ブロック
			e.printStackTrace();
			return null;
		}//try
	}//public static BufferedReader getFileReader(String fileName)

	public static String readAllContent(BufferedReader br) {
		String		line;					/* read line		*/
		String		content	= "";		/* content read from br	*/
		
		try {
			line = br.readLine();
		} catch (IOException e) {
			// TODO 自動生成された catch ブロック
			e.printStackTrace();
			return null;
		}
		
		while (line != null) {
			content 	+= (line + "\n");
			try {
				line			= br.readLine();
			} catch (IOException e) {
				// TODO 自動生成された catch ブロック
				e.printStackTrace();
				return null;
			}
		}//while (content != null)
		return content;
		
	}//public String elemType readAllContent(BufferedReader br)
}//public class STDLIB
