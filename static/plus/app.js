$(function() {
    //model

    var A_article=Backbone.Model.extend(
    {
      initialize:function(){},
      url:'/latest'
    });
    var a_article=new A_article();
    var articles=new Array();
    a_article.fetch({
      success:function(model,response){
        $(response).each(function(i){
           $('#links').append("<li><a href='#article/"+i+"'>"+this.title+"</a></li>");
           articles[i]=this;
        })
          $('#brand').html(articles[0]['article']);
          $('#title').html(articles[0]['title']);
          $('#time').html(articles[0]['pubdate']);
          $('#content').html(articles[0]['descr']+articles[0]['content']);
          $('#from').html('<h5 style="color:#A36D6D"><b>转自：'+articles[0]['article']+'</b><span><a href="'+articles[0]['link']+'" style="float:right;color:#A36D6D" target="_blank"><i class="glyphicon glyphicon-eye-open"></i>查看原文</a></span></h5>');
      },
      error:function(){
        console.log("err")
      }
    })

    //router
    var $divShow=$("#content");
    var $divTitle=$("#title");
    var $divTime=$("#time");
    var $divFrom=$("#from");
    //action方式触发
    var testrouter=Backbone.Router.extend({
      routes:{
        '':'main',
        'article/:key':'article_read',
        'yige':'yige',
        '36kr':'kr36',
        'douban':'douban',
        'geekpark':'geekpark',
      },
      main:function(){
        $divTitle.html(articles[0]['title']);
        $divTime.html(articles[0]['pubdate']);
        $divShow.html(articles[0]['descr']+articles[0]['content']);
        $divFrom.html('<h5 style="color:#A36D6D"><b>转自：'+articles[0]['article']+'</b><span><a href="'+articles[0]['link']+'" style="float:right;color:#A36D6D" target="_blank"><i class="glyphicon glyphicon-eye-open"></i>查看原文</a></span></h5>')
      },
      article_read:function(key){
        $divTitle.html(articles[key]['title']);
        $divTime.html(articles[key]['pudate']);
        $divShow.html(articles[key]['descr']+articles[key]['content']);
        $divFrom.html('<h5 style="color:#A36D6D"><b>转自：'+articles[key]['article']+'</b><span><a href="'+articles[key]['link']+'" style="float:right;color:#A36D6D" target="_blank"><i class="glyphicon glyphicon-eye-open"></i>查看原文</a></span></h5>')
      },
      yige:function(){
        var B_article=Backbone.Model.extend(
        {
          initialize:function(){},
          url:'/yige'
        });
        var b_article=new B_article();
        $("#links").html('');
        b_article.fetch({
          success:function(model,response){
          $(response).each(function(i){
             $('#links').append("<li><a href='#article/"+i+"'>"+this.title+"</a></li>");
             articles[i]=this;
            })
            $('#brand').html(articles[0]['article']);
            $('#title').html(articles[0]['title']);
            $('#time').html(articles[0]['pubdate']);
            $('#content').html(articles[0]['descr']+articles[0]['content']);
            $('#from').html('<h5 style="color:#A36D6D"><b>转自：'+articles[0]['article']+'</b><span><a href="'+articles[0]['link']+'" style="float:right;color:#A36D6D" target="_blank"><i class="glyphicon glyphicon-eye-open"></i>查看原文</a></span></h5>');
        },
        error:function(){
          console.log("err")
        }
      })
      },
      kr36:function(){
        var C_article=Backbone.Model.extend(
        {
          initialize:function(){},
          url:'/36kr'
        });
        var c_article=new C_article();
        $("#links").html('');
        c_article.fetch({
          success:function(model,response){
          $(response).each(function(i){
             $('#links').append("<li><a href='#article/"+i+"'>"+this.title+"</a></li>");
             articles[i]=this;
            })
            $('#brand').html(articles[0]['article']);
            $('#title').html(articles[0]['title']);
            $('#time').html(articles[0]['pubdate']);
            $('#content').html(articles[0]['descr']+articles[0]['content']);
            $('#from').html('<h5 style="color:#A36D6D"><b>转自：'+articles[0]['article']+'</b><span><a href="'+articles[0]['link']+'" style="float:right;color:#A36D6D" target="_blank"><i class="glyphicon glyphicon-eye-open"></i>查看原文</a></span></h5>');
        },
        error:function(){
          console.log("err")
        }
      })
      },
       douban:function(){
        var D_article=Backbone.Model.extend(
        {
          initialize:function(){},
          url:'/douban'
        });
        var d_article=new D_article();
        $("#links").html('');
        d_article.fetch({
          success:function(model,response){
          $(response).each(function(i){
             $('#links').append("<li><a href='#article/"+i+"'>"+this.title+"</a></li>");
             articles[i]=this;
            })
            $('#brand').html(articles[0]['article']);
            $('#title').html(articles[0]['title']);
            $('#time').html(articles[0]['pubdate']);
            $('#content').html(articles[0]['descr']+articles[0]['content']);
            $('#from').html('<h5 style="color:#A36D6D"><b>转自：'+articles[0]['article']+'</b><span><a href="'+articles[0]['link']+'" style="float:right;color:#A36D6D" target="_blank"><i class="glyphicon glyphicon-eye-open"></i>查看原文</a></span></h5>');
        },
        error:function(){
          console.log("err")
        }
      })
      },
      geekpark:function(){
        var E_article=Backbone.Model.extend(
        {
          initialize:function(){},
          url:'/geekpark'
        });
        var e_article=new E_article();
        $("#links").html('');
        e_article.fetch({
          success:function(model,response){
          $(response).each(function(i){
             $('#links').append("<li><a href='#article/"+i+"'>"+this.title+"</a></li>");
             articles[i]=this;
            })
            $('#brand').html(articles[0]['article']);
            $('#title').html(articles[0]['title']);
            $('#time').html(articles[0]['pubdate']);
            $('#content').html(articles[0]['descr']+articles[0]['content']);
            $('#from').html('<h5 style="color:#A36D6D"><b>转自：'+articles[0]['article']+'</b><span><a href="'+articles[0]['link']+'" style="float:right;color:#A36D6D" target="_blank"><i class="glyphicon glyphicon-eye-open"></i>查看原文</a></span></h5>');
        },
        error:function(){
          console.log("err")
        }
      })
      },
    });
    var router=new testrouter();
    Backbone.history.start();

  });