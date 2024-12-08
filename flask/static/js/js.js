var btnradio = 0;
window.onload = function() {
    document.getElementById("btnradio1").onclick = function() {
        if(btnradio!=1){
            var txt = document.getElementById("btnradiolbl1").innerHTML;
            document.getElementById("InputText").value = txt;
            document.getElementById("select1").selectedIndex = 1;
            document.getElementById("select2").selectedIndex = 1;
            btnradio = 1;
        } else if(btnradio==1) {
            document.getElementById("btnradio1").checked = false;
            document.getElementById("InputText").value = null;
            document.getElementById("select1").selectedIndex = null;
            document.getElementById("select2").selectedIndex = null;            
            btnradio = 0;
        }        
    };
    document.getElementById("btnradio2").onclick = function() {
        if(btnradio!=2){
            var txt = document.getElementById("btnradiolbl2").innerHTML;
            document.getElementById("InputText").value = txt;
            document.getElementById("select1").selectedIndex = 1;
            document.getElementById("select2").selectedIndex = 2;            
            btnradio = 2;
        } else if(btnradio==2) {
            document.getElementById("btnradio2").checked = false;
            document.getElementById("InputText").value = null;
            document.getElementById("select1").selectedIndex = null;
            document.getElementById("select2").selectedIndex = null;              
            btnradio = 0;
        }        
    };
    document.getElementById("btnradio3").onclick = function() {
        if(btnradio!=3){
            var txt = document.getElementById("btnradiolbl3").innerHTML;
            document.getElementById("InputText").value = txt;
            document.getElementById("select1").selectedIndex = 2;
            document.getElementById("select2").selectedIndex = 2;            
            btnradio = 3;
        } else if(btnradio==3) {
            document.getElementById("btnradio3").checked = false;
            document.getElementById("InputText").value = null;
            document.getElementById("select1").selectedIndex = null;
            document.getElementById("select2").selectedIndex = null;              
            btnradio = 0;
        }        
    };        
    document.getElementById("submit_btn").onclick = function() {
        var cnt = 0;
        localStrage = window.localStorage;
        sessionStrage = window.sessionStorage;
        if(!localStorage.getItem("cnt")){            
            localStorage.setItem("cnt",0);
        } else {
            var cnt_str = localStrage.getItem("cnt");
            cnt = parseInt(cnt_str,10);
        }
        var auth_key = sessionStrage.getItem("auth_key");
        var select1 = document.getElementById("select1").selectedIndex;
        var select2 = document.getElementById("select2").selectedIndex;
        var inputtxt = document.getElementById("InputText").value;

        document.getElementById("answer").innerText = null;
        document.getElementById("spinner").style.display = "block";
        var request = new XMLHttpRequest();        
        var payload = "ans_accuracy=" + select1 + "&ans_length=" + select2 + "&InputText=" + inputtxt + "&Count=" + cnt + "&AuthKey=" + auth_key;

        request.onload = function(){
            var data = this.response;
            document.getElementById("spinner").style.display = "none";
            document.getElementById("answer").innerHTML = data;
            cnt++;
            localStorage.setItem("cnt",String(cnt));              
        }
        request.open('POST', "/", true)
        request.timeout = 0;
        request.setRequestHeader( 'Content-Type', 'application/x-www-form-urlencoded' );
        request.send(payload);
    };
};