import sqlite3

#######################
# Sample Project Data #
#######################
data_projects_json = {
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


def get_project_details_by_id(uid):
    return data_projects_json['project_id'][f'{uid}']


def get_all_projects():
    return data_projects_json['project_id']


def get_bom_by_project_name():
    pass


def post_new_project(title, compDate, ownerName):
    next_project_id = str(len(get_all_projects().keys()))

    data_projects_json['project_id'][next_project_id] = {
        'title': title,
        'compDate': compDate,
        'ownerName': ownerName,
        'status': 'open'
    }

    return data_projects_json['project_id'][next_project_id]
