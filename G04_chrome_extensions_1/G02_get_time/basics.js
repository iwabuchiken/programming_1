function show_time(){
  var now = new Date();
//  str = typeof(now);  // => object
  var t = new Array(6);
  t[0] = now.getFullYear();
  t[1] = now.getMonth() + 1;
  t[2] = now.getDate();
  t[3] = now.getHours();
  t[4] = now.getMinutes();
  t[5] = now.getSeconds();
  for (var i = 0; i < t.length; i++ ) {
    t[i] = String(t[i]);
    if (t[i].length < 2) {t[i] = "0" + t[i]};
//    if (len(t[i]) < 2) {t[i] = "0" + t[i]};
  }
  
//  var target = document.getElementById("time_label");
  var label = t.slice(0,3).join("/") + "-"
//  var label = t.slice(0,3).join("//") + "-"
        + t.slice(3, t.length).join(":");
//  target.innerHTML = label;
  var target2 = document.getElementById("inputbox");
//  var label2 = t.slice(0,3).join("/") + "-"
//        + t.slice(3, t.length).join(":");
  target2.setAttribute("value", label);
//  target.innerHTML = t.slice(0,2).join("-")
//  target.innerHTML = t.join("-");
//  str = typeof(str);  // => number
//  str = "typeof str";
//  str = typeof str;  // => number
//  str = String(str);  //
//  var len = str.length; //=> 4
//  str = typeof str; //=> string
//  str = "typeof(str)";

//  str = now.getFullYear() + "/"
//      + (now.getMonth()+1) + "/"
//      + now.getDate() + "-"
//      + now.getHours() + ":"
//      + now.getMinutes() + ":"
//      + now.getSeconds();
//  var target = document.getElementById("time_label");
//  target.innerHTML = len;
//  target.innerHTML = str;
}

function get_focus(name) {
  document.form1.inputbox.focus();
//  document.form1.name.focus();
}