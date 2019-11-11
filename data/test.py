test=[
{
            "http://cso.kmi.open.ac.uk/schema/cso#superTopicOf": [
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/artificial_intelligence"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/robotics"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/computer_vision"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/hardware"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/computer_operating_systems"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/computer_networks"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/bioinformatics"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/software_engineering"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/information_technology"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/data_mining"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/information_retrieval"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/computer_programming"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/human_computer_interaction"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/human-computer_interaction"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/computer_aided_design"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/computer-aided_design"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/computer_security"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/theoretical_computer_science"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/computer_system"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/computer_systems"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/internet"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/computer_hardware"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/software"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/formal_languages"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/computer_network"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/computer_communication_networks"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/operating_system"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/operating_systems"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/cad"
            },
            {
                "@id": "https://cso.kmi.open.ac.uk/topics/computer_aided_design_%28cad%29"
            }
        ],
}
]
if len(test):
    # print(test[0]['http://cso.kmi.open.ac.uk/schema/cso#superTopicOf'])
    print(list(set([record['@id']+'.json' for record in test[0]['http://cso.kmi.open.ac.uk/schema/cso#superTopicOf']])))
        # print(test[0]['http://cso.kmi.open.ac.uk/schema/cso#superTopicOf'][record])
    # for key in test[0]['http://cso.kmi.open.ac.uk/schema/cso#superTopicOf']:
    #     print(test[0]['http://cso.kmi.open.ac.uk/schema/cso#superTopicOf'][key])
    # print([ test[0]['http://cso.kmi.open.ac.uk/schema/cso#superTopicOf'][key] for key in test[0]['http://cso.kmi.open.ac.uk/schema/cso#superTopicOf']])
else:
    print(0)