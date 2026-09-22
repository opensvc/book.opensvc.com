// Tabs.
//
// A page shows how to do a thing with the command line, and the same thing
// through the api. Both belong on the page, and only one belongs on the
// screen: the reader is doing one or the other.
//
// The markup is written in the page as
//
//     <div class="tabs">
//     <div class="tab" data-title="CLI">
//     ...markdown...
//     </div>
//     <div class="tab" data-title="API">
//     ...markdown...
//     </div>
//     </div>
//
// With no javascript the panes render one after the other, each under its own
// heading, which is the whole content in reading order rather than a broken
// control.
//
// The choice is remembered, and applies to every group on every page: a
// reader who came for the api came for the api.
(function () {
  var KEY = "opensvc.tab";

  function remembered() {
    try {
      return window.localStorage.getItem(KEY);
    } catch (e) {
      return null;
    }
  }

  function remember(title) {
    try {
      window.localStorage.setItem(KEY, title);
    } catch (e) {
      /* a reader who blocks storage just picks again */
    }
  }

  function select(group, title) {
    group.querySelectorAll(":scope > .tab").forEach(function (pane) {
      pane.classList.toggle("tab-selected", pane.dataset.title === title);
    });
    group.querySelectorAll(":scope > .tab-bar > button").forEach(function (button) {
      var on = button.textContent === title;
      button.classList.toggle("tab-selected", on);
      button.setAttribute("aria-selected", on ? "true" : "false");
    });
  }

  function build(group) {
    var panes = Array.prototype.slice.call(group.querySelectorAll(":scope > .tab"));
    if (panes.length < 2) {
      return;
    }
    var titles = panes.map(function (pane) {
      return pane.dataset.title || "";
    });
    var bar = document.createElement("div");
    bar.className = "tab-bar";
    bar.setAttribute("role", "tablist");
    titles.forEach(function (title) {
      var button = document.createElement("button");
      button.type = "button";
      button.setAttribute("role", "tab");
      button.textContent = title;
      button.addEventListener("click", function () {
        remember(title);
        // Every group moves together: the reader picked a way of working,
        // not a pane of one example.
        document.querySelectorAll(".tabs").forEach(function (other) {
          select(other, title);
        });
      });
      bar.appendChild(button);
    });
    group.insertBefore(bar, panes[0]);
    group.classList.add("tabs-ready");

    var wanted = remembered();
    select(group, titles.indexOf(wanted) >= 0 ? wanted : titles[0]);
  }

  function init() {
    document.querySelectorAll(".tabs").forEach(build);
  }

  // The script is loaded at the end of the body, so the document is still
  // parsing when it runs. Reading the state rather than assuming it keeps the
  // tabs working if it is ever loaded deferred or injected.
  if (document.readyState === "loading") {
    window.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
