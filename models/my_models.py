from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Models for the database for each position group
# Each positon group have different stats for their specific position 
# Thats why creating a model for each positon group would be easier to serialize

# You don't have to initialize the database and serializer right away 
db = SQLAlchemy()
ma = Marshmallow()

"""
Create the models with the specific things you want
One to many relationship
    - You connect the different models(db.relationship with the name of the Model, and 
    create variable(player) to connect with the stats )

Marshmallow - Used to serialize the database objects to send that as a json
Schema()
 - ma.SQLAlchemyAutoSchema to automatically connect with the database
"""

class WRModels(db.Model):
    __tablename__ = 'wr_models' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    team = db.Column(db.String, nullable=False)
    number = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    stats = db.relationship('WRStats',backref='player')

class WRStats(db.Model): 
    __tablename__ = 'wr_stats'
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String, nullable=False)
    games = db.Column(db.String, nullable=False)
    receptions = db.Column(db.String, nullable=False)
    targets = db.Column(db.String, nullable=False)
    yards = db.Column(db.String, nullable=False)
    avgYards = db.Column(db.String, nullable=False)
    tds = db.Column(db.String, nullable=False)
    longestRec = db.Column(db.String, nullable=False)
    receivingFirstDowns = db.Column(db.String, nullable=False)
    fumbles = db.Column(db.String, nullable=False)
    rushingFumbleLost = db.Column(db.String, nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('wr_models.id'), nullable=False)
      
class WRSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WRModels

class WRStatsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WRStats


class QBModels(db.Model):
    __tablename__ = 'qb_models'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String, nullable=True)
    team = db.Column(db.String, nullable=False)
    number = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    stats = db.relationship('QBStats',backref='player')



class QBStats(db.Model):
    __tablename__ = 'qb_stats'
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String, nullable=False)
    games = db.Column(db.String, nullable=False)
    completions = db.Column(db.String, nullable=False)
    attempts = db.Column(db.String, nullable=False)
    completionPercent = db.Column(db.String, nullable=False)
    yards = db.Column(db.String, nullable=False)
    avgYards = db.Column(db.String, nullable=False)
    tds = db.Column(db.String, nullable=False)
    ints = db.Column(db.String, nullable=False)
    longestPass = db.Column(db.String, nullable=False)
    sacks = db.Column(db.String, nullable=False)
    fumbles = db.Column(db.String, nullable=False)
    passerRating = db.Column(db.String, nullable=False)
    qbr = db.Column(db.String, nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('qb_models.id'), nullable=False)

class QBSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = QBModels

class QBStatsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = QBStats

class RBModels(db.Model):
    __tablename__ = 'rb_models'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String, nullable=True)
    team = db.Column(db.String, nullable=False)
    number = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    stats = db.relationship('RBStats',backref='player')

class RBStats(db.Model):
    __tablename__ = 'rb_stats'
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String, nullable=False)
    games = db.Column(db.String, nullable=False)
    attempts = db.Column(db.String, nullable=False)
    yards = db.Column(db.String, nullable=False)
    avgYards = db.Column(db.String, nullable=False)
    tds = db.Column(db.String, nullable=False)
    longestRun = db.Column(db.String, nullable=False)
    rushing1stDowns = db.Column(db.String, nullable=False)
    fumbles = db.Column(db.String, nullable=False)
    rushingFumbleLost = db.Column(db.String, nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('rb_models.id'), nullable=False)


class RBSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RBModels

class RBStatsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RBStats

# LineBackers, Dline and DBs have the same stat sheet
class DefenseModels(db.Model):
    __tablename__ = 'defense_models'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String, nullable=True)
    team = db.Column(db.String, nullable=False)
    number = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    stats = db.relationship('DefenseStats',backref='player')

class DefenseStats(db.Model):
    __tablename__ = 'defense_stats'
    id = db.Column(db.Integer,primary_key=True)
    year = db.Column(db.String, nullable=False)
    games = db.Column(db.String, nullable=False)
    total = db.Column(db.String, nullable=False)
    solo = db.Column(db.String, nullable=False)
    ast = db.Column(db.String, nullable=False)
    sacks = db.Column(db.String, nullable=False)
    forcedFumbles = db.Column(db.String, nullable=False)
    fumblesRecovered = db.Column(db.String, nullable=False)
    fumbleYards = db.Column(db.String, nullable=False)
    interceptions = db.Column(db.String, nullable=False)
    intYards = db.Column(db.String, nullable=False)
    avgYardsIntercepted = db.Column(db.String, nullable=False)
    tds = db.Column(db.String, nullable=False)
    longestInterception = db.Column(db.String, nullable=False)
    passDef = db.Column(db.String, nullable=False)
    stuffs = db.Column(db.String, nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('defense_models.id'), nullable=False)

class DefenseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DefenseModels

class DefenseStatsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DefenseStats
