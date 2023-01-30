document.addEventListener("DOMContentLoaded", function (event) {
    console.log("Ready");

    const imageType=()=>{
    let type = window.location.pathname
    type=type.replace("/","")
    type=type.split("to")
    return{input:type[0], output:type[1]}
    }
    console.log(imageType().output)


    const errorMessage = document.getElementById("error-message");
    let selectionArea = document.querySelector('#select-area')
    let fileInput = document.querySelector('#image');
    let preview = document.getElementById('file-preview');
    let convert = document.getElementById('convert-button');
    let removeImage = document.getElementById('remove-img');
    removeImage.style.display = "none";
    
    if  (imageType().input==="jpg"){
      fileInput.accept=`image/jpeg`
    }else{
      fileInput.accept=`image/${imageType().input}`
    }

    removeImage.addEventListener("click", () => {
      fileInput.value = null;
      preview.src = null;
      preview.style.display = "none";
      removeImage.style.display = "none";
      selectionArea.style.display = null;
      convert.classList.remove("tada")
      convert.disabled = true;
    })

    selectionArea.addEventListener("click", () => {      
      fileInput.click();
    });

    convert.addEventListener("click", () => {
      convertToPNG()
    })

    fileInput.onchange = ({
      target
    }) => {
      let check = checkImage()
      if (check === true) {
        console.log('checkimage')
        let file = target.files[0];
        let image_url = URL.createObjectURL(file);
        preview.src = image_url;
        selectionArea.style.display = 'none';
        removeImage.style.display = null;
        preview.style.display = null;
      }
      else return false
    }

    function checkImage(context) {
      var image = document.getElementById("image").files[0];
      let t=`image/${imageType().input}`
      
      if (image) {
        if (image.size > 5000000) {
          mensagem("Image is too large. Maximum size is 5MB.");
          return false
        } else if (image.type !== t) {
          mensagem(`Selected file is not a ${t.input} image.`);
          return false
        } else {
          convert.disabled = false;
          convert.classList.add("tada")

          return true
        }
      } else mensagem("Escolha uma imagem para a conversão")
    }

    function convertToPNG() {
      console.log("start check")
      var image = document.getElementById("image").files[0];
      if (!image) {
        mensagem("Please select an image.");
        return;
      }
      var formData = new FormData();
      formData.append("image", image);
      fetch(`/api${ window.location.pathname}`, {
        method: "POST",
        body: formData
      }).then(response => response.blob())
        .then(blob => {
          console.log(blob)
          const url = URL.createObjectURL(blob);
          const link = document.createElement("a");
          link.href = url;
          link.download = `image.${imageType().output}`;
          link.click();
          removeImage.click();
        })
        .catch(error => {
          mensagem("Ocorreu um erro na conversão da imagem.")             
        });
    }

  });

  function mensagem(mensagem) {
    let mensagemContainer = document.getElementById("mensagem-container");
    let errorMessage = document.getElementById("error-message");
    errorMessage.innerHTML = mensagem;
    mensagemContainer.style.display = "block";
    setTimeout(function () {
      mensagemContainer.style.display = "none";
    }, 5000)
  }