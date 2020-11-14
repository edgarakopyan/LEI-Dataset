import pandas as pd
import xml.etree.ElementTree as etree
import os
import numpy as np


os.getcwd()
os.chdir('/Users/edgarakopyan/Desktop/ESG Project')
tree = etree.parse("20201013-gleif-concatenated-file-lei2.xml")
root = tree.getroot()

LEI = []
Legal_Name = []
Other_Name = []
LA_First_line = []
LA_Additional_line = []
LA_City = []
LA_Region = []
LA_Country = []
LA_Postcode = []
HQ_First_line = []
HQ_Additional_line = []
HQ_City = []
HQ_Region = []
HQ_Country = []
Other_First_line = []
Other_Additional_line = []
Other_City = []
Other_Region = []
Other_Country = []
Other_Postcode = []
RA_ID = []
RA_Entity_ID = []
RA_Legal_Jurisdiction = []
Legal_Form_Code = []
Other_Legal_Form = []
Entity_Status = []
Initial_Registration_Date = []
Last_Update = []
Registration_Status = []
Next_Renewal_date = []
Managing_LOU = []
Validation_Sources = []
Validation_Authority_ID = []

for i in range(0, 1723692):
   try:
      LEI.append(root[1][i][0].text )
   except IndexError:
      LEI.append('NA')

   try:
      Legal_Name.append(root[1][i][1][0].text)
   except IndexError:
      Legal_Name.append('NA')

   try:
      Other_Name.append(root[1][i][1][1][0].text)
   except IndexError:
      Other_Name.append('NA')

   try:
      LA_First_line.append(root[1][i][1][2][0].text)
   except:
      LA_First_line.append('NA')

   try:
      LA_Additional_line.append(root[1][i][1][2][1].text)
   except IndexError:
      LA_Additional_line.append('NA')

   try:
      LA_City.append(root[1][i][1][2][2].text)
   except IndexError:
      LA_City.append('NA')

   try:
      LA_Region.append(root[1][i][1][2][3].text)
   except:
      LA_Region.append('NA')

   try:
      LA_Country.append(root[1][i][1][2][4].text)
   except IndexError:
      LA_Country.append('NA')

   try:
      LA_Postcode.append(root[1][i][1][2][5].text)
   except IndexError:
      LA_Postcode.append('NA')

   try:
      HQ_First_line.append(root[1][i][1][2][0].text)
   except:
      HQ_First_line.append('NA')

   try:
      HQ_Additional_line.append(root[1][i][1][2][1].text)
   except IndexError:
      HQ_Additional_line.append('NA')
   try:
      HQ_City.append(root[1][i][1][2][2].text)
   except IndexError:
      HQ_City.append('NA')
   try:
      HQ_Region.append(root[1][i][1][2][3].text)
   except IndexError:
      HQ_Region.append('NA')
   try:
      HQ_Country.append(root[1][i][1][2][4].text)
   except IndexError:
      HQ_Country.append('NA')
   try:
      Other_First_line.append(root[1][i][1][2][0].text)
   except IndexError:
      Other_First_line.append('NA')
   try:
      Other_Additional_line.append(root[1][i][1][2][1].text)
   except IndexError:
      Other_Additional_line.append('NA')
   try:
      Other_City.append(root[1][i][1][2][2].text)
   except IndexError:
      Other_City.append('NA')
   try:
      Other_Region.append(root[1][i][1][2][3].text)
   except IndexError:
      Other_Region.append('NA')
   try:
      Other_Country.append(root[1][i][1][2][4].text)
   except IndexError:
      Other_Country.append('NA')
   try:
      Other_Postcode.append(root[1][i][1][2][5].text)
   except IndexError:
      Other_Postcode.append('NA')
   try:
      RA_ID.append(root[1][i][1][5][0].text)
   except IndexError:
      RA_ID.append('NA')
   try:
      RA_Entity_ID.append(root[1][i][1][5][1].text)
   except IndexError:
      RA_Entity_ID.append('NA')
   try:
      RA_Legal_Jurisdiction.append(root[1][i][1][6].text)
   except IndexError:
      RA_Legal_Jurisdiction.append('NA')
   try:
      Legal_Form_Code.append(root[1][i][1][7][0].text)
   except IndexError:
      Legal_Form_Code.append('NA')
   try:
      Other_Legal_Form.append(root[1][i][1][7][1].text)
   except IndexError:
      Other_Legal_Form.append('NA')
   try:
      Entity_Status.append(root[1][i][1][8].text)
   except IndexError:
      Entity_Status.append('NA')
   try:
      Initial_Registration_Date.append(root[1][i][2][0].text)
   except IndexError:
      Initial_Registration_Date.append('NA')
   try:
      Last_Update.append(root[1][i][2][1].text)
   except IndexError:
      Last_Update.append('NA')
   try:
      Registration_Status.append(root[1][i][2][2].text)
   except IndexError:
      Registration_Status.append('NA')
   try:
      Next_Renewal_date.append(root[1][i][2][3].text)
   except IndexError:
      Next_Renewal_date.append('NA')
   try:
      Managing_LOU.append(root[1][i][2][4].text)
   except IndexError:
      Managing_LOU.append('NA')
   try:
      Validation_Sources.append(root[1][i][2][5].text)
   except IndexError:
      Validation_Sources.append('NA')
   try:
      Validation_Authority_ID.append(root[1][i][2][6][0].text)
   except IndexError:
      Validation_Authority_ID.append('NA')

df = pd.DataFrame()
df['LEI'] = LEI
df['Legal Name'] = Legal_Name
df['Other Name'] = Other_Name
df['Legal Address First line'] = LA_First_line
df['Legal Address Additional line'] = LA_Additional_line
df['Legal Address City'] = LA_City
df['Legal Address Region'] = LA_Region
df['Legal Address Country'] = LA_Country
df['Legal Address Postcode'] = LA_Postcode
df['Headquarters First line'] = HQ_First_line
df['Headquarters Additional line'] = HQ_Additional_line
df['Headquarters City'] = HQ_City
df['Headquarters Region'] = HQ_Region
df['Headquarters Country'] = HQ_Country
df['Other Address First line'] = Other_First_line
df['Other Address Additional line'] = Other_Additional_line
df['Other Address City'] = Other_City
df['Other Address Region'] = Other_Region
df['Other Address Country'] = Other_Country
df['Other Address Postcode'] = Other_Postcode
df['Registration Status'] = Registration_Status
df['Initial Registration Date'] = Initial_Registration_Date
df['Registration Authority ID'] = RA_ID
df['Registration Authority Entity ID'] = RA_Entity_ID
df['Registration Authority Legal Jurisdiction'] = RA_Legal_Jurisdiction
df['Legal Form Code'] = Legal_Form_Code
df['Other Legal Form'] = Other_Legal_Form
df['Entity Status'] = Entity_Status
df['Initial Registration Date']= Initial_Registration_Date
df['Last Update'] = Last_Update
df['Registration Status'] = Registration_Status
df['Next Renewal Date'] = Next_Renewal_date
df['Managing LOU'] = Managing_LOU
df['Validation Sources'] = Validation_Sources
df['Validation Authority ID'] = Validation_Authority_ID


df1 = df[:1000000]
df2 = df[1000000:]
df1.to_excel("LEI_Dataset_Part_1.xlsx")
df2.to_excel("LEI_Dataset_Part_2.xlsx")

df1.to_csv("LEI_Dataset_Part_1.csv")
df2.to_csv("LEI_Dataset_Part_2.csv")




for i in range(0, 1723692):
   Legal_Name.append(root[0][i][1][0].text)

for i in range(0, 1723692):
   LEI.append(root[0][i][0].text)

for i in range(0, 1723692):
   Registration_Status.append(root[0][i][2][2].text)

for i in range(0, 1723692):
   Initial_Registration_Date.append(root[0][i][2][0].text)

for i in range(0, 1723692):
   try:
      LA_Country.append(root[0][i][1][2][4].text)
   except IndexError:
      LA_Country.append('NA')


os.getcwd()
os.chdir('/Users/edgarakopyan/Desktop/ESG Project')
tree = etree.parse("20201013-gleif-concatenated-file-rr.xml")
root = tree.getroot()


StartNodeID = []
StartNodeIDType = []
EndNodeID = []
EndNodeIDType = []
RelationshipType = []
RelationshipPeriodStartDate = []
RelationshipPeriodEndDate = []
PeriodType = []
RelationshipPeriodStartDate2 =[]
Periodtype2 = []
RelationshipStatus = []
RelationshipQualifierDimension = []
QualifierCategory = []
RelationshipQuantifierMeasurementMethod = []
QuantifierAmount = []
QuantifierUnits = []
InitialRegistrationDate = []
LastUpdateDate = []
RegistrationStatus = []
NextRenewalDate = []
ManagingLOU = []
ValidationSources = []
ValidationDocuments = []
ValidationReference = []


for i in range(0, 224910):
   try:
      StartNodeID.append(root[1][i][0][0][0].text)
   except IndexError:
      StartNodeID.append('NA')

   try:
      StartNodeIDType.append(root[1][i][0][0][1].text)
   except IndexError:
      StartNodeIDType.append('NA')

   try:
      EndNodeID.append(root[1][i][0][1][0].text)
   except IndexError:
      EndNodeID.append('NA')

   try:
      EndNodeIDType.append(root[1][i][0][1][1].text)
   except IndexError:
      EndNodeIDType.append('NA')

   try:
      RelationshipType.append(root[1][i][0][2].text)
   except IndexError:
      RelationshipType.append('NA')

   try:
      RelationshipPeriodStartDate.append(root[1][i][0][3][0][0].text)
   except IndexError:
      RelationshipPeriodStartDate.append('NA')

   try:
      RelationshipPeriodEndDate.append(root[1][i][0][3][0][1].text)
   except IndexError:
      RelationshipPeriodEndDate.append('NA')

   try:
      PeriodType.append(root[1][i][0][3][0][2].text)
   except IndexError:
      PeriodType.append('NA')

   try:
      RelationshipPeriodStartDate2.append(root[1][i][0][3][1][0].text)
   except IndexError:
      RelationshipPeriodStartDate2.append('NA')

   try:
      Periodtype2.append(root[1][i][0][3][1][1].text)
   except IndexError:
      Periodtype2.append('NA')

   try:
      RelationshipStatus.append(root[1][i][0][4].text)
   except IndexError:
      RelationshipStatus.append('NA')

   try:
      RelationshipQualifierDimension.append(root[1][i][0][5][0][0].text)
   except IndexError:
      RelationshipQualifierDimension.append('NA')

   try:
      QualifierCategory.append(root[1][i][0][5][0][1].text)
   except IndexError:
      QualifierCategory.append('NA')

   try:
      RelationshipQuantifierMeasurementMethod.append(root[1][i][0][6][0][0].text )
   except IndexError:
      RelationshipQuantifierMeasurementMethod.append('NA')

   try:
      QuantifierAmount.append(root[1][i][0][6][0][1].text)
   except IndexError:
      QuantifierAmount.append('NA')

   try:
      QuantifierUnits.append(root[1][i][0][6][0][2].text)
   except IndexError:
      QuantifierUnits.append('NA')

   try:
      InitialRegistrationDate.append(root[1][i][1][0].text)
   except IndexError:
      InitialRegistrationDate.append('NA')

   try:
      LastUpdateDate.append(root[1][i][1][1].text)
   except IndexError:
      LastUpdateDate.append('NA')

   try:
      RegistrationStatus.append(root[1][i][1][2].text)
   except IndexError:
      RegistrationStatus.append('NA')

   try:
      NextRenewalDate.append(root[1][i][1][3].text)
   except IndexError:
      NextRenewalDate.append('NA')

   try:
      ManagingLOU.append(root[1][i][1][4].text)
   except IndexError:
      ManagingLOU.append('NA')

   try:
      ValidationSources.append(root[1][i][1][5].text)
   except IndexError:
      ValidationSources.append('NA')

   try:
      ValidationDocuments.append(root[1][i][1][6].text)
   except IndexError:
      ValidationDocuments.append('NA')

   try:
      ValidationReference.append(root[1][i][1][7].text)
   except IndexError:
      ValidationReference.append('NA')

dfrel = pd.DataFrame()
dfrel['Start Node ID'] = StartNodeID
dfrel['Start Node ID Type'] = StartNodeIDType
dfrel['End Node ID'] = EndNodeID
dfrel['End Node ID Type']  = EndNodeIDType
dfrel['Relationship Type'] = RelationshipType
dfrel['Relationship Period Start Date']  = RelationshipPeriodStartDate
dfrel['Relationship Period End Date'] = RelationshipPeriodEndDate
dfrel['Period Type'] = PeriodType
dfrel['Relationship Period Start Date 2'] = RelationshipPeriodStartDate2
dfrel['Period type 2'] = Periodtype2
dfrel['Relationship Status'] = RelationshipStatus
dfrel['Relationship Qualifier Dimension'] = RelationshipQualifierDimension
dfrel['Qualifier Category'] = QualifierCategory
dfrel['Relationship Quantifier Measurement Method'] = RelationshipQuantifierMeasurementMethod
dfrel['Quantifier Amount'] = QuantifierAmount
dfrel['Quantifier Units'] = QuantifierUnits
dfrel['Initial Registration Date'] = InitialRegistrationDate
dfrel['Last Update Date'] = LastUpdateDate
dfrel['Registration Status'] = RegistrationStatus
dfrel['Next Renewal Date'] = NextRenewalDate
dfrel['Managing LOU'] = ManagingLOU
dfrel['Validation Sources'] = ValidationSources
dfrel['Validation Documents'] = ValidationDocuments
dfrel['Validation Reference'] = ValidationReference

dfrel.to_csv("Relationship Data.csv")
dfrel.to_excel("Relationship Data.xlsx")



os.getcwd()
os.chdir('/Users/edgarakopyan/Desktop/ESG Project')
tree = etree.parse("20201013-gleif-concatenated-file-repex.xml")
root = tree.getroot()

root[1][i][0].text # LEI
root[1][i][1].text # Exception Category
root[1][i][2].text # Exception Reason

LEI = []
ExceptionCategory = []
ExceptionReason = []


for i in range(0, 2864218):
   try:
      LEI.append(root[1][i][0].text)
   except IndexError:
      LEI.append('NA')

   try:
      ExceptionCategory.append(root[1][i][1].text)
   except IndexError:
      ExceptionCategory.append('NA')

   try:
      ExceptionReason.append(root[1][i][2].text)
   except IndexError:
      ExceptionReason.append('NA')

dfexc = pd.DataFrame()
dfexc['LEI'] = LEI
dfexc['Exception Category'] = ExceptionCategory
dfexc['Exception Reason'] = ExceptionReason

df1, df2, df3 = np.array_split(dfexc, 3)
df1.to_csv("Exception Part 1.csv")
df2.to_csv("Exception Part 2.csv")
df3.to_csv("Exception Part 3.csv")
