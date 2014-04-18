if ( typeof $.fn.tabs !== 'undefined') {
    // just to make sure we can access jquerytools tabs when $.fn.tabs is overriden by jqueryui
    // requires jquerytools to be loaded before jqueryui
    $.fn.jqtTabs = $.fn.tabs;
}
