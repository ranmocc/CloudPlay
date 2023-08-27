var table_status = false;
var table = $('#table');
var arrow = $('.arrow');
table.hide();
arrow.hide();
//创建按钮单击事件，表单显隐切换
$('#control_video').click( ()=>{
    if (!table_status){
        table.show();
        arrow.show();
        table_status = true;
    }
    else{
        table.hide();
        arrow.hide();
        table_status = false;
    }
});

//获取url中参数值
function GetQueryValue(queryName) {
    debugger;
    //提取url的？后的参数（不包含？）
    var query = decodeURI(window.location.search).substring(1);
    console.log(query)
    //split将query以“&”进行分割，为字符串数组arr
    var arr = query.split("&");
    for (var i = 0; i < arr.length; i++) {
        var param = arr[i].split("=");
        if (param[0] === queryName) {
            return param[1];
        }
    }
    return null;
}
// 表单提交按钮响应事件
var error = GetQueryValue('error')
if(error!=null){
    var url = window.location
    var newurl = url.toString().split("?");
    console.log(newurl);
    alert(error);
    // history.go(-1);
    window.location=newurl[0];
}

//获取table中的status元素
// var statusList = $('.status')
// debugger
// for (var j = 0;j<statusList.length;j++){
//     j.innerText = j.innerText?"上线中":"已下线"
// }


// console.log("-----test------")
// console.log($('.status'))
// console.log(statusText)

// $('.add').click(()=>{
//     if(error!=null){
//         alert(error);
//         window.location.search=null
//     }
// })

