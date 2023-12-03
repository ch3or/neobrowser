// side tab
side_tab_enabled = true;
const side_tab = document.getElementById("side-tab");
const tela = document.getElementById("window");
function check_side_tab() {
    if (side_tab_enabled == true) {
        side_tab.style.display = "block";
    }
    else {
        side_tab.style.display = "none";
    }
}
check_side_tab();
document .addEventListener("keydown", (event) => {
    if ((event. ctrlKey || event. metaKey) && event. key === "q") {
        if (side_tab_enabled == true){
            side_tab_enabled = false;
        }
        else {
            side_tab_enabled = true;
        }
        check_side_tab();

    }
});

// track mouse movement
document.addEventListener('mousemove', function(e){
    x = e.clientX;
    y = e.clientY;
});

function main(){
    window.src = "cheor.com.br";
}
main();

webView.getEngine().loadContent("cheor.com.br")