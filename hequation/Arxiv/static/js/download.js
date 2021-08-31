function setSelectAllBox(){
    var selectAllBox = document.getElementsByName("selectAllBox")[0];
    if(this.checked==false){
        selectAllBox.checked=false;
    }
    else{
        var i;
        var boxs = document.getElementsByName("downloadCheckBox")
        for(i=0;i<boxs.length;i++){
            if(boxs[i].checked==false){
                selectAllBox.checked=false;
                return;
            }
        }
        selectAllBox.checked=true;
    }
}


function selectAllCheckBox(){
    var boxs = document.getElementsByName("downloadCheckBox")
    var selectAllBox = document.getElementsByName("selectAllBox")[0]
    var i;
    for(i=0;i<boxs.length;i++){
        boxs[i].checked = selectAllBox.checked;
    }
}

function reverseAllCheckBox(){
    var boxs = document.getElementsByName("downloadCheckBox");
    var selectAllBox = document.getElementsByName("selectAllBox")[0];
    var i;
    var flag=true;
    for(i=0;i<boxs.length;i++) {
        boxs[i].checked = !boxs[i].checked;
        console.log(boxs[i].checked)
        if(boxs[i].checked==false){
            console.log(boxs[i].checked)
            selectAllBox.checked=false;
            flag=false;
        }
    }
    console.log(flag)
    if(flag==true){
        selectAllBox.checked=true;
    }

}

function downloadChecked(){
    var boxs = document.getElementsByName("downloadCheckBox")
    var i
    var cnt=0
    for(i=0;i<boxs.length;i++){
        if(boxs[i].checked) {
            cnt++;
        }

    }
    var res = confirm("Are you sure to download these "+ cnt+" files")
    if(res==false){
        return
    }
    for(i=0;i<boxs.length;i++){
        if(boxs[i].checked){
            var param = boxs[i].value.split("HXL", 2)
            console.log(param[0])
            console.log(param[1])
            downloadFileByUrlAndName(param[0], param[1])
        }
    }
}

//通过资源url下载文件，将文件命名为pdfname
function downloadFileByUrlAndName(url, pdfname){
    var config = {
        url:url,
        responseType:'blob'
    }
    axios.request(config).then(function (response) {
        saveBlobFile(response.data, pdfname);
    })
    .catch(function (error) {
        console.log(error);
    });
}

//保存文件
function saveBlobFile(BlobData,fileName){
    var export_blob = new Blob([BlobData])
    var blobURL = window.URL.createObjectURL(export_blob)
    // 创建a标签，用于跳转至下载链接
    const tempLink = document.createElement('a')
    tempLink.style.display = 'none'
    tempLink.href = blobURL
    tempLink.setAttribute('download', fileName)
    // 挂载a标签
    document.body.appendChild(tempLink)
    tempLink.click()
    document.body.removeChild(tempLink)
    // 释放blob URL地址
    window.URL.revokeObjectURL(blobURL)
}

function testfunc() {
    c1 = document.getElementsByName("1")
    c2 = document.getElementsByName("2")
    alert(c1.prop(checked))
    alert(c2.checked)
}