let selectclass = document.querySelector("#selectclass");

let knight = document.querySelector("#knight");
let knight_stats = document.querySelector("#knight_stats")

let rogue = document.querySelector("#rogue");
let rogue_stats = document.querySelector("#rogue_stats");


let mage = document.querySelector("#mage");
let mage_stats = document.querySelector("#mage_stats");


let sprite = document.querySelector("#sprite");
selectclass.onchange = function(){
    console.log(selectclass.value);

    if(selectclass.value == "knight"){
        knight.style.display = "block";
        knight_stats.style.display = "block";

        rogue.style.display = "none";
        rogue_stats.style.display = "none";

        mage.style.display = "none";
        mage_stats.style.display = "none";
    }
    else if(selectclass.value == "rogue"){
        knight.style.display = "none";
        knight_stats.style.display = "none";

        mage.style.display = "none";
        mage_stats.style.display = "none";

        rogue.style.display = "block";
        rogue_stats.style.display = "block";
    }
    else if(selectclass.value == "mage"){
        knight.style.display = "none";
        knight_stats.style.display = "none";

        rogue.style.display = "none";
        rogue_stats.style.display = "none";

        mage.style.display = "block";
        mage_stats.style.display = "block";
    }
    else{
        knight.style.display = "none";
        knight_stats.style.display = "none";

        rogue.style.display = "none";
        rogue_stats.style.display = "none";

        mage.style.display = "none";
        mage_stats.style.display = "none";
    }
}

// function toggle(){
//     if(knight);
// }






