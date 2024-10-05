from django.db import models

class Member(models.Model):
  givenName = models.CharField(max_length=255)
  middleInitial = models.CharField(max_length=3, blank=True)
  lastName = models.CharField(max_length=255)
  reviewerTeam = models.BooleanField(default=False)
  potdTeam = models.BooleanField(default=False)
  creativesTeam = models.BooleanField(default=False)
  externalsTeam = models.BooleanField(default=False)
  bio1 = models.BooleanField(default=False)
  chem1 = models.BooleanField(default=False)
  phys1 = models.BooleanField(default=False)
  math3 = models.BooleanField(default=False)
  stat = models.BooleanField(default=False)
  cs3 = models.BooleanField(default=False)
  eng3 = models.BooleanField(default=False)
  fil3 = models.BooleanField(default=False)
  ss3 = models.BooleanField(default=False)

  def __str__(self):
    return f"{self.givenName} {self.middleInitial} {self.lastName}"

  def listTeams(self):
    out = []
    if self.reviewerTeam == True:
      out.append("Reviewer Team")
    if self.potdTeam == True:
      out.append("PoTD Team")
    if self.creativesTeam == True:
      out.append("Creatives Team")
    if self.externalsTeam == True:
      out.append("Externals Team")
    return out

  def listSubjects(self):
    out = []
    if self.bio1 == True:
      out.append("Biology 1")
    if self.chem1 == True:
      out.append("Chemistry 1")
    if self.phys1 == True:
      out.append("Physics 1")
    if self.math3 == True:
      out.append("Mathematics 3")
    if self.stat == True:
      out.append("Statistics")
    if self.cs3 == True:
      out.append("Computer Science 3")
    if self.eng3 == True:
      out.append("English 3")
    if self.fil3 == True:
      out.append("Filipino 3")
    if self.ss3 == True:
      out.append("Social Science 3")
    return out