data_current_projects = [
                            ("Bird Mansion", "11-25-25", "J. Morrison"),
                            ("Wickham Park Renovation", "12-15-25", "P. Williams"),
                            ("Canova Beach Jetty", "3-29-26", "B. Douglas")
                        ]

next_project_id = 7

data_current_projects_json = {
    'project_id': {
        '1': {
            'title': 'Bird Mansion',
            'compDate': '11-25-25',
            'ownerName': 'J. Morrison',
            'status': 'open'
        },
        '2': {
            'title': 'Wickham Park Renovation',
            'compDate': '12-15-25',
            'ownerName': 'P. Williams',
            'status': 'open'
        },
        '3': {
            'title': 'Canova Beach Jetty',
            'compDate': '3-29-26',
            'ownerName': 'B. Douglas',
            'status': 'open'
        },
        '4': {
            'title': 'Plumbing Melbourne',
            'compDate': '10-13-22',
            'ownerName': 'J. Morrison',
            'status': 'closed'
        },
        '5': {
            'title': 'Skatepark Addition',
            'compDate': '1-15-23',
            'ownerName': 'J. Morrison',
            'status': 'closed'
        },
        '6': {
            'title': 'Hurricane Cleanup',
            'compDate': '3-29-23',
            'ownerName': 'B. Douglas',
            'status': 'closed'
        },
    }
}


data_project_bom = [
                                ("1", "2", "5", "0"),
                                ("1", "3", "15", "5"),
                                ("1", "4", "20", "20"),
                                ("2", "1", "5", "5"),
                                ("2", "6", "1", "1"),
                                ("3", "4", "20", "20"),
                            ]

data_past_projects = [
                            ("Plumbing Melbourne", "10-13-22", "J. Morrison"),
                            ("Skatepark Addition", "1-15-23", "J. Morrison"),
                            ("Hurricane Cleanup", "3-29-23", "B. Douglas")
                        ]