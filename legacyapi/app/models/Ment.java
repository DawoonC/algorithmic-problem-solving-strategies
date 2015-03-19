package models;

import java.util.List;

public class Ment	{
	private String id;
	
//	private PhotoMent<List> photoMent;
//	private TextMent textMent;
	
//	private String type;	//	photo/photos, ment, mentwcontent, file/files, video, share
	private String resouceUri;
//	type: photo/photos, ment, file/files, video, share
//	resource: url
//	shared_content
//	mentions ? (content로…)
//	photos
//	files
	
	private Where where;
	private Writer writer;
	private String content;
	private MentCount mentCount;
	private String version;	//	created_at
	private String privacy; // privacy (공개설정)
	private boolean isAnnounced;	//is_announced (공지글이냐?)
	private boolean isFavorited;	//is_favorited (나의 관심을?)
	private boolean islitup;	//is_litup (나의 빛내기?)
	
	private List<ClasstingUser> litupPeople;	//litup_people (이름, id 3개까지만)
	private AccessMent accessMent;	//	access (수정권한)
	private String topic;
	private List<Comment> comments;
}
