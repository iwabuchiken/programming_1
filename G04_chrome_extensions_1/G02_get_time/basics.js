function show_time(){
  var now = new Date();
//  str = typeof(now);  // => object
  var t = new Array(6);
  
  t[0] = now.getFullYear(); t[1] = now.getMonth() + 1;
  t[2] = now.getDate(); t[3] = now.getHours();
  t[4] = now.getMinutes(); t[5] = now.getSeconds();
  
  for (var i = 0; i < t.length; i++ ) {
    t[i] = String(t[i]);
    if (t[i].length < 2) {t[i] = "0" + t[i]};
  }//for (var i = 0; i < t.length; i++ ) {

  var label = t.slice(0,3).join("/") + "-"
        + t.slice(3, t.length).join(":");
  var label2 = t.slice(0,3).join("") + "_"
        + t.slice(3, t.length).join("");
    //set time label to the inputbox
  var target = document.getElementById("inputbox");
  target.setAttribute("value", label);
  var target2 = document.getElementById("inputbox2");
  target2.setAttribute("value", label2);
}//function show_time()

function get_focus(name) {
  //document.form1.inputbox.focus();
  document.form2.inputbox2.focus();
//  document.form1.name.focus();
}