window.onload = function() {
    document.getElementById("unlimited_btn").onclick = function() {
        var inputtxt = document.getElementById("InputText").value;
        var request = new XMLHttpRequest();        
        var payload = "Password=" + inputtxt;

        request.onload = function(){
            var data = this.response;
            if(data=="unmatch"){
                alert("パスワードが違います");
                return;
            }
            window.sessionStorage.setItem("auth_key",data);              
            window.location.href = "/";
        }
        request.open('POST', "/unlimited", true)
        request.setRequestHeader( 'Content-Type', 'application/x-www-form-urlencoded' );
        request.send(payload);
    };    
    document.getElementById("form1").onkeypress = (e) => {
        // form1に入力されたキーを取得
        const key = e.keyCode || e.charCode || 0;
        // 13はEnterキーのキーコード
        if (key == 13) {
          // アクションを行わない
          e.preventDefault();
        }
      }    
};