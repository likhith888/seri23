from pymongo import MongoClient

conn = MongoClient('mongodb+srv://likhith888:7Ax76jTp79W6yfBK@clusterseri0.sscrgoa.mongodb.net/?retryWrites=true&w=majority')

db_users = conn.seri.users
db_projects = conn.seri.projects
