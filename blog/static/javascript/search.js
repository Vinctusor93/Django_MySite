function s(value,object) {
    var parameter1 = $('script[src*="search.js"]').data('parameter_1');
    console.log("create post is working!"+value)
    $.ajaxSetup({
    headers: { "X-CSRFToken": parameter1 }
    });
    $.ajax({
        url : location.href, // the endpoint
        type : "POST", // http method
        data : { 'type' : value ,'objects' : object}, // data sent with the post request
        success : function(json) {  // handle a successful response


            console.log(json); // another sanity check
            if(json['type'] == 'Manga'){
                       td_manga = document.getElementsByClassName("td-manga");

            for(var index=0;index<td_manga.length;index++){

              console.log("confronto "+td_manga[index].id+" e "+ json + "e il risultato e "+ json['manga'].includes(td_manga[index].id));
              if(!json['manga'].includes(td_manga[index].id))
                  td_manga[index].style.display = 'none';
              else
                  td_manga[index].style.display = 'initial';

            }
            }
            else if(json['type'] == 'Game'){

             td_game = document.getElementsByClassName("td-games");
             console.log(td_game);
            for(var index=0;index<td_game.length;index++){

              console.log("confronto "+td_game[index].id+" e "+ json + "e il risultato e "+ json['game'].includes(td_game[index].id));
              if(!json['game'].includes(td_game[index].id))
                  td_game[index].style.display = 'none';
              else
                  td_game[index].style.display = 'initial';

            }
          }
        }, //finish success

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};