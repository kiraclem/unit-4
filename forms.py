from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length

class TeamForm(FlaskForm):
    team_name = StringField('your team name', validators=[DataRequired(), Length(min=4,max=45)])
    submit = SubmitField('submit')

class ProjectForm(FlaskForm):
    project_name = StringField('your project name?', validators=[DataRequired(), Length(min=4, max=100)])
    description = TextAreaField('description')
    completed = BooleanField('is your project complete?')
    team_selection = SelectField('team')
    submit = SubmitField('submit')

    def update_teams(self, teams):
        self.team_selection.choices = [ (team.id, team.team_name) for team in teams ]
