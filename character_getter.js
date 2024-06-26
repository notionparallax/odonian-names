// Character getter
// The characters are described on litcharts.com
// here: https://www.litcharts.com/lit/the-dispossessed/characters
// run this in the console to get some json of their names and descriptions
JSON.stringify(Array.from(document.querySelectorAll(".character")).map(
    (x) => {
        return {
            "character_name": x.querySelector(".name").innerText,
            "character_description": x.querySelector("div:not(.name)").innerText
        }
    }
))