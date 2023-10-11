const changeTheme = document.getElementById("theme-btn");
var cnt = 0;
// 0-green, 1-red, 2-blue
const colorCode = ['#27AE60',"#ff0800","#0ef"]

if(!localStorage.getItem("colorCnt"))
    document.body.style.setProperty("--color-secondary", colorCode[0]);
else {
    document.body.style.setProperty("--color-secondary", colorCode[localStorage.getItem("colorCnt")]);
    cnt = localStorage.getItem("colorCnt");
}


changeTheme.addEventListener("click", () => {
    cnt = (cnt+1)%3;
    // console.log(cnt,"->",colorCode[cnt])
    localStorage.setItem("colorCnt",cnt)
    document.body.style.setProperty("--color-secondary", colorCode[localStorage.getItem("colorCnt")]);
});