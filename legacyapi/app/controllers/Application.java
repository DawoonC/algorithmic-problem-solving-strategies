package controllers;

import play.*;
import play.mvc.*;

import views.html.*;

public class Application extends Controller {

    public static Result getNewsFeed() {
    	
    	return ok( "Get NewsFeed!!!" );
    }
	
	
    public static Result index() {
    	return ok("200");
//        return ok(index.render("Your new application is ready."));
    }

}
