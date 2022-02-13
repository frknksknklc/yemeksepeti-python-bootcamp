from DatabaseProcess.DbOperations import DbOperations
from FileProcess.DataParser import DataParser
from argparse import ArgumentParser
argparser=ArgumentParser()
argparser.add_argument("--json_path", "--file", type=str, required=True)
argparser.add_argument("--db_path", "--db", type=str, required=True)
args = argparser.parse_args()

json_path=args.json_path
db_path=args.db_path

dp=DataParser(json_path)
allusers=dp.createUsersFromJSON()

dbops=DbOperations(db_path)
dbops.createTable()
dbops.insertUserList(allusers)