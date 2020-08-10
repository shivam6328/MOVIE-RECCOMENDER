let button = document.querySelector('.btn')

// movie name entered by the user.
let movieName = document.querySelector('.inputValue')

function addTable(columnNames, dataArray) {
  var recom=document.createElement('h3');
  var valuesss=document.createTextNode("HERE ARE YOUR RECCOMENDATIONS");
  recom.appendChild(valuesss);
  document.body.appendChild(recom);
  //var data = JSON.parse(this.response)
  var myTable = document.createElement("table");
  
  document.body.appendChild(myTable);

  var y = document.createElement("tr");
  myTable.appendChild(y);

  for(var i = 0; i < columnNames.length; i++) {
    var th = document.createElement("th"),
    columns = document.createTextNode(columnNames[i]);
    th.appendChild(columns);
    y.appendChild(th);
  }

  //var newValue = dataArray[1][0];
  //document.getElementById("test").innerHTML = newValue;


  for(var i =0 ; i < dataArray.length ; i++) {
    var row= dataArray[i];
    var y2 = document.createElement("tr");
    for(var j = 0 ; j < row.length; j++) {
      myTable.appendChild(y2);
      if (j==1){
        //myTable.appendChild(y2);
        var a=document.createElement("a");
        var th2 = document.createElement("td");
        var date2 = document.createTextNode(row[j]);
        var link=row[2];
        a.appendChild(date2);
        a.title=row[j];
        a.href=link;
        th2.appendChild(a);
        y2.appendChild(th2);
      }
      else if (j!=2){
      //myTable.appendChild(y2);
      var th2 = document.createElement("td");
      var date2 = document.createTextNode(row[j]);
      th2.appendChild(date2);
      y2.appendChild(th2);
      }
    }
    if (row.length==3){
      //myTable.appendChild(y2);
      var th2 = document.createElement("td");
      var date2=document.createTextNode("not available");
      th2.appendChild(date2);
      y2.appendChild(th2);
    }

  }

}

button.addEventListener('click' , function(){
    //document.getElementById("movieTitle").innerHTML = "HERE ARE YOUR RECCOMENDATIONS";
    console.log(movieName.value);
 //var value is undefined by default
 url='http://127.0.0.1:5000/';
 const optns = {
   method: 'POST',
   body: JSON.stringify(movieName.value),
   mode: 'no-cors'
}

// send POST request
fetch(url, optns)
   .then(res => res.json())
   .then(res => console.log(res));
 //let request=new XMLHttpRequest()
 //request.open('POST','http://127.0.0.1:5000/',true);
 //request.send(JSON.stringify('Heat (1995)'));
 //console.log(JSON.stringify('Heat (1995)'))
 //file = fopen("demofile3.txt", 3);
 //fwrite(file,'Heat (1995)');
 //console.log('here');
 //let request=new XMLHttpRequest()
 //fetch('/api/geocode')
 //.then((res)=>{ console.log(res) })
 let request=new XMLHttpRequest()
 request.open('GET','http://127.0.0.1:5000/',true);
 
 //request.send(JSON.stringify('Heat (1995)'));
 //request.send();
 //let fin;
 request.onload = function() {
   // Begin accessing JSON data here
   var data = JSON.parse(this.response)
   console.log(data);
   //window.value=data;
   //document.getElementById("recoms").innerHTML = data;
   var list = ["MOVIE ID","TITLE","GENRE"];
   addTable(list,data);
  
 }

 request.send();
 //document.getElementById("recoms").innerHTML = window.value;
 console.log('here');
})
console.log(movieName.value);
//document.getElementById("recoms").innerHTML = data;
 //var value is undefined by default
 /*url='http://127.0.0.1:5000/';
 const optns = {
   method: 'POST',
   body: JSON.stringify(movieName.value),
}

*/
/* //addTable*/