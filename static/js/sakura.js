
function search(){
    if (document.getElementById("searchInput").value == ""){
        document.getElementById("errors").innerHTML = "Không được để trống"
        document.getElementById("collapseExample").setAttribute("class","collaspe show")
    }
    else{
        let value = document.getElementById("searchInput").value
        let url = "/sakura/api/card/"+value+""
        document.getElementById("searchInput").value = ""
        fetch(url)
            .then(function(respone){
                return respone.json();
            })
            .then(function(data){
                if (data['nameCard'] == "-1"){
                    document.getElementById("errors").innerHTML = "Không tìm thấy lá bạn yêu cầu"
                    document.getElementById("collapseExample").setAttribute("class","collaspe show")
                }
                else{
                    document.getElementById("collapseExample").setAttribute("class","collapse")
                    document.getElementById("clow").src=data["link_clow"]
                    document.getElementById("sakura").src=data["link_sakura"]
                    document.getElementById("namecard").innerHTML="<p style=\"font-size: 24px;\"><b>"+data['nameCard']+"</b></p>"
                    document.getElementById("sign").innerHTML="<p><b>Hệ:</b> "+data['sign']+"</p>"
                    document.getElementById("magictype").innerHTML="<p><b>Loại phép:</b> "+data['magicType']+"</p>"
                    document.getElementById("capturedA").innerHTML="<p><b>Tập anime xuất hiện:</b> "+data['capturedAnime']+"</p>"
                    document.getElementById("capturedM").innerHTML="<p><b>Tập manga xuất hiện:</b> "+data['capturedManga']+"</p>"
                    document.getElementById("transformedA").innerHTML="<p><b>Tập anime biến đổi:</b> "+data['transformedAnime']+"</p>"
                    document.getElementById("transformedM").innerHTML="<p><b>Tập manga biến đổi:</b> "+data['transformedManga']+"</p>"
                    console.log(data)
                }
                
            })
    }
    
    
    // document.getElementById("searchInput").value = ""
}