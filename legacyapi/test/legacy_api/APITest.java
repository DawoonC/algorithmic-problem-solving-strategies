package legacy_api;

import static org.junit.Assert.*; 
import junit.framework.TestCase;

import org.junit.Test;

import com.jayway.restassured.RestAssured;
import com.jayway.restassured.config.DecoderConfig;
import com.jayway.restassured.config.EncoderConfig;
import com.jayway.restassured.config.RestAssuredConfig;

public class APITest extends TestCase	{

	@Override
	protected void setUp() throws Exception {
		RestAssured.baseURI = "http://localhost:9001";
		
		RestAssured.config = new RestAssuredConfig().
			decoderConfig(
				new DecoderConfig("UTF-8")
			).encoderConfig(
				new EncoderConfig("UTF-8", "UTF-8")
			);
		
		super.setUp();
	}

	@Test
	public void testGetNewsFeed() throws Exception {
		String jsonResponse = RestAssured.
			when().
				get( "/newsfeed" ).asString();
		
		System.out.println( "response in GET: " + jsonResponse );
		
		assertTrue( jsonResponse.contains("NewsFeed!!!") );
	}
}
