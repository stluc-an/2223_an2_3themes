window.addEventListener("load", function() {



asideL = document.querySelector("aside#left")
asideR = document.querySelector("aside#right")

references = document.querySelectorAll("main article .footnote-ref")

alternate = false

// current total offset in asideL or asideR
let totalOffset = [0,0]

for (let ref of references){
	console.log(ref.hash);

	refOffset = ref.offsetTop

	fnLi = document.querySelector(ref.hash.replace(":","\\:"))
	fnImg = fnLi.querySelector("img")
	fnImg.id = fnLi.id
	fnImg.title = fnImg.alt

	if(!alternate){
		asideL.appendChild(fnImg)
		asideSide = 0
	}
	else{
		asideR.appendChild(fnImg)
		asideSide = 1
	}
	alternate = !alternate

	fnImgHeight = fnImg.offsetHeight
	console.log(`current total ${totalOffset[asideSide]}`)
	console.log(`refOffset ${refOffset} + fnImgHeight ${fnImgHeight}`)


	// what's the difference between the elt offset and the current offset in that aside?
	diff = Math.max(0,refOffset - totalOffset[asideSide])
	// if diff<0, we want actually a diff of 0, which will avoid overlap

	// we update the total
	totalOffset[asideSide] = refOffset+fnImgHeight
	console.log(`new total ${totalOffset[asideSide]}`)

	fnImg.style.marginTop = diff + "px"

	fnLi.remove()
	ref.remove()
}

document.querySelector("article .footnote").remove()

});
