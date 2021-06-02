const imagesToPdf = require("images-to-pdf");


let images = Array.from(new Array(90).keys()).map((a,i) => "./place-cards/"+i+".png");
console.log(images);


(async() => {
    await imagesToPdf(images, 'combined.pdf');
})()
