//Dataset Example
//companies = ['Microsoft','Google','Amazon','IBM','Deloitte','Capgemini','Amdocs']
//recruitments = [120, 150, 180, 90, 110, 130, 80]

//(a) Bar Chart
plt.bar(companies, recruitments)
plt.title("Company Recruitment")
plt.xticks(rotation=30)
plt.show()

//(b) Pie Chart
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()

//(c) Customized Pie Chart
colors = ['red','blue','green','yellow','purple','orange','cyan']

plt.pie(recruitments, labels=companies, colors=colors,
        autopct='%1.1f%%', startangle=140)

plt.title("Customized Pie Chart")
plt.show()

//(d) Doughnut Chart
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')

centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("Doughnut Chart")
plt.show()

//(e) Compare IBM vs Amdocs
names = ['IBM','Amdocs']
values = [90, 80]

plt.bar(names, values)
plt.title("IBM vs Amdocs Recruitment")
plt.show()
