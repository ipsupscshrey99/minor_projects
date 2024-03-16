const hourEl = document.getElementById("Hours");
const minuteEl = document.getElementById("Minutes");
const secondEl=document.getElementById("seconds");
const ampmEl=document.getElementById("AMPM");

function updateClock(){
    let h = new Date().getHours();
    let m = new Date().getMinutes();
    let s = new Date().getseconds();
    let AMPM = "AM"

    if(h > 12){
        h = h - 12;
        AMPM = "PM"; 

    }
    hourEl.innerText = h; 
    minuteEl.innerText = m;
    secondEl.innerText = s;
    ampmEl.innerText = AMPM;

    setTimeout(()=>{
        updateClock();
    },1000 )


}
