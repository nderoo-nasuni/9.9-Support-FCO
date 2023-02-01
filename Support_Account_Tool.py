import csv
# For help contact Nick DeRoo

# Running
# python3 Support_Account_Tool.py

def main():

    # put your input and output filenames here:
    #This is the list of affected customers
    input_file = "affected_customers.csv"
    #this is the list of 9.9 customers which we are checking against.
    customers = "accounts.csv"
    output_file = "CVM_Affected_Customers_upgraded_to_99.csv"

    header = ["Account ID",	"Company/Name",	"Filer", "ID", "Signup", "Last Activity", "Churned" "Build", "GUID", "Cloud Capacity", "Files", "Subscription"]
    results = []
    with open(input_file, 'r') as f, open(customers, 'r') as customers, open(output_file, 'w') as outf:
        customers = csv.reader(customers, delimiter=',')
        affected_customers = csv.reader(f, delimiter=',')
        writer = csv.writer(outf)
        results.append(header)
        affected_customers_list = []
        for a in affected_customers:
            affected_customers_list.append(a[0])
        for customer in customers:
            if customer[1] in affected_customers_list:
                results.append(customer)
        for row in results:
            writer.writerow(row)
if __name__ == "__main__":
    main()