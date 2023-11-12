title "Tests MySQL"

control 'MySQL Installation' do
 impact 1.0
 title 'Check if mysql is installed with be_installed'
 desc 'Use should be_installed to test mysql'

 describe package('mysql-server') do
   it { should be_installed }
 end
end

control 'mysql Configuration File' do
 impact 1.0
 title 'Check if mysql is installed'
 desc 'test to chels'

 describe file("/etc/mysql/my.cnf") do
   it {should be_file}
 end
end

control 'mysql-Version' do
 impact 1.0
 title 'mysql-version'
 desc 'test for checking mysql version'

 describe package('mysql-server') do
   its('version') { should cmp >= '8.0.35*'}
 end
end

control 'mysql is running' do
 impact 1.0
 title 'Check if mysql is running'
 desc 'Test if the mysql service is running'

 describe service('mysql') do
  it { should be_enabled }
  it { should be_running }
 end

 describe port(3306) do
  it { should be_listening }
 end

end

control 'mysql is running (test without systemctl)' do
  impact 1.0
  title 'Check if mysql is running using "service" command'
  desc 'Test if the mysql service is running'

  describe command ('service mysql status') do
    its ('exit_status') {should eq 0}
 end
end