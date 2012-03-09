# -*- coding: utf-8 -*-
import sys
sys.path.append("d:\python\sharejs")

from mysqldb import DB
from model.topic import Topic

class TopicRepository(DB):
    def __init__(self):
        DB.__init__(self)

    def get_data(self,topic_id):
        self.cursor.execute('select * from topic where topicid=%(topicid)s',{'topicid':topic_id})
        topic_dict = self.cursor.fetchone()
        if topic_dict:
            return Topic(topic_dict)
        else:
            return None

    def get_all_topic(self):
        self.cursor.execute('select * from topic')
        topic_dict_list = self.cursor.fetchall()
        if topic_dict_list:
            return map(lambda topic_dict:Topic(topic_dict),topic_dict_list)
        else:
            return None

if __name__== "__main__":
    topic_repository  = TopicRepository()
    with topic_repository  :
        print(topic_repository.get_data(1).title)
