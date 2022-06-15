
  $(function() {
    $( "#picker" ).datepicker();
  } );

function showPreview(event){
  if(event.target.files.length > 0){
    var src = URL.createObjectURL(event.target.files[0]);
    var file = event.target.files[0],
    fileName = file.name,
    fileSize = file.size;
    const fruits = ["png", "jpeg", "jpg"];
    var info = document.getElementById("info");
    var preview = document.getElementById("file-ip-1-preview");
    const ext_Array = fileName.split(".");
    if (ext_Array.length <1){
      preview.src = ""
      info.innerHTML = "Invalid Image format"
      return 
    }
    var extension = ext_Array[ext_Array.length-1];

    if(fileSize/1000000 >= 5){
      preview.src = ""
      info.innerHTML = "Image is too big"
    }
    if (fruits.includes(extension)){
      info.innerHTML=""
      preview.src = src;
      preview.style.display = "block";
      preview.style.height = "50px";
      preview.style.width = "60px";
      preview.style.float = "right"
    }
    else{
      preview.src = ""
      info.innerHTML = "Invalid Image format"
      return
    }

    
    
    
  }
}