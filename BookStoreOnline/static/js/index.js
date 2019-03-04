$(function(){
	//设置首页按钮背景（点击样式）
	$(".click_bg:eq(0)")
	.css({"background-image":"url(../img/sdc_icon.png)",
		"background-position":"left -272px",
		"background-repeat":"no-repeat"		
	});
	// 左侧菜单悬停显示
	$(".left_menu_mini:eq(0)").hover(function(){
		$(".second_level:eq(0)").animate({height:"show",opacity:"show"},400);
		},function(){
		$(".second_level:eq(0)").hide();
	});
	$(".left_menu_mini:eq(1)").hover(function(){
		$(".second_level:eq(1)").animate({height:"show",opacity:"show"},400);
		},function(){
		$(".second_level:eq(1)").hide();
	});
	//轮播
	//文字悬停
	$(".loop_text").css("opacity","0.6");
	$(".bigpic").hover(function(){
		$(".loop_text").animate({opacity:"1"},300);
	},function(){
		$(".loop_text").animate({opacity:"0.6"},300);
	});
	//初始化界面
	$(".bigpic").hide();
	$(".bigpic:eq(0)").show();
	$(".loop_minipic_small img:eq(0)").css("opacity","0.4");
	var i= 0;//创建索引
	//右键
	$(".loop .loop_bigpic .rig").click(function(){
		$(".loop_minipic_small img").animate({opacity:"1"},200);
		$(".bigpic").fadeOut(500);
		if(i<5){
			i++;
		}else{
			i=0;
		}
		$(".loop_minipic_small img:eq("+i+")").animate({opacity:"0.4"},200);
		$(".bigpic:eq("+i+")").fadeIn(500);
	});
	//左键
	$(".loop .loop_bigpic .lef").click(function(){
		$(".loop_minipic_small img").animate({opacity:"1"},200);
		$(".bigpic").fadeOut(500);
		if(i>0){
			i--;
		}else{
			i=5;
		}
		$(".loop_minipic_small img:eq("+i+")").animate({opacity:"0.4"},200);
		$(".bigpic:eq("+i+")").fadeIn(500);
	});
	// 点击切换
	$(".loop_minipic_small").click(function(){
		i=$(this).index();
		$(".loop_minipic_small img").animate({opacity:"1"},200);
		$(".bigpic").fadeOut(500);
		$(".loop_minipic_small img:eq("+i+")").animate({opacity:"0.4"},200);
		$(".bigpic:eq("+i+")").fadeIn(500);
	});
	// 定时器定时轮播
	var k=setInterval(function(){
			$(".rig").click();
		},5000);
	// 图片悬停出现阅读按钮
	$(".hotEssay .hotEssay_main .mini .pic").hover(function(){
		$(this).children(".read").show();
	},function(){
		$(this).children(".read").hide();
	});
	// 搜索框点击
	$("html").click(function(){
		var isFocus=$(".find").is(":focus");  
    	if(true==isFocus){  
        	$(".chicken").animate({top:"-24px"},300);
        	$(".find").val("");
    	}else{  
        	$(".chicken").animate({top:"0"},300);
        	$(".find").val("憋说话，搜我");
        }
	});	
	// tag标签悬停
	$(".orange_tag_head_mini").hover(function(){
		$(".orange_tag_head_mini .span .text").css("color","#525252");
		$("#span_one").css("background-position","5px -30px");
		$("#span_two").css("background-position","5px -190px");
		$("#span_three").css("background-position","5px -110px");
		$(".orange_tag_head_mini").css("background","none");
		$(this).css("background","#FE4800");
		$(this).children(".span").children(".text").css("color","white");
		$(".orange_tag_main").hide();
		if($(this).attr("id")=="orange_tag_head_mini1")
		{	

			$("#span_one").css("background-position","5px 10px");
			$("#orange_tag_main1").show();
		}else if($(this).attr("id")=="orange_tag_head_mini2")
		{
			$("#span_two").css("background-position","5px -150px");
			$("#orange_tag_main2").show();
		}else if($(this).attr("id")=="orange_tag_head_mini3")
		{
			$("#span_three").css("background-position","5px -70px");
			$("#orange_tag_main3").show();
		}
	});
	// 初始化第一个标签
	$(".orange_tag_head_mini:eq(0)").mouseover();
	// 跟随屏幕滚动的广告
	$(document).scroll(function(){
		if($(document).scrollTop()>=2052){
			$(".ad_newui")
			.css({
				position:"fixed",
				top:"0px"
			});
		}else if($(document).scrollTop()<2052){
			$(".ad_newui")
			.css({
				position:"",
				top:""
			});
		}
	});
	//跟随屏幕滚动的top按钮
	$(document).scroll(function(){
		if($(document).scrollTop()>0){
			$(".top").fadeIn(500);
		}else if($(document).scrollTop()==0){
			$(".top").fadeOut(500);
		}
	});
	// 分享
	$(".share_big").hover(function(){
		$(this).animate({right:"0px"},500);
	},function(){
		$(this).animate({right:"-226px"},500);
	})
	// 小图标悬停改变背景位置
		$(".wanwang").hover(function(){
			$(this).animate({"background-position-x":"-1px",
							"background-position-y":"-25px"},300);
		},function(){
			$(this).animate({"background-position-x":"-1px",
							"background-position-y":"0px"},300);
		});
		$(".wei").hover(function(){
			$(this).animate({"background-position-x":"-52px",
							"background-position-y":"-25px"},300);
		},function(){
			$(this).animate({"background-position-x":"-52px",
							"background-position-y":"0px"},300);
		});
		$(".sina").hover(function(){
			$(this).animate({"background-position-x":"-77px",
							"background-position-y":"-25px"},300);
		},function(){
			$(this).animate({"background-position-x":"-77px",
							"background-position-y":"0px"},300);
		});
		$(".tengxunweibo").hover(function(){
			$(this).animate({"background-position-x":"-84px",
							"background-position-y":"-75px"},300);
		},function(){
			$(this).animate({"background-position-x":"-84px",
							"background-position-y":"-51px"},300);
		});
		$(".qiniu").hover(function(){
			$(this).animate({"background-position-x":"-108px",
							"background-position-y":"-25px"},300);
		},function(){
			$(this).animate({"background-position-x":"-108px",
							"background-position-y":"-0px"},300);
		});
});