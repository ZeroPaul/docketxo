

app
//==================================
// ui app routers
//==================================
    .config(function($stateProvider) {

    $stateProvider
    //==================================
    // ui layout base
    //==================================
        .state('dock', {
        url: '/dock',
        views: {
            '': {
                templateUrl: 'app/views/layout.html'
            },
            'aside': {
                templateUrl: 'app/views/aside.html'
            },
            'content': {
                templateUrl: 'app/views/content.html'
            }
        }
    })

    //==================================
    // test1
    //==================================
    .state("dock.docente", {
        url: "/docente",
        data: { section: 'DocketPro', page: 'Docentes' },
        templateUrl: "ioteca_web_apps/docket/views/test.html",
    })
    
    // .state("dock.test", {
    //     url: "/ct",
    //     data: { section: 'System', page: 'Document' },
    //     templateUrl: "ioteca_web_apps/docket/views/test.html"
    // }) 

   
    ;
});
