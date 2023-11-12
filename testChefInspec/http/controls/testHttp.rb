title "Tests HTTP (Apache2)"

control 'Apache2 Installation' do
 impact 1.0
 title 'Check if apache2 is installed with be_installed'
 desc 'Use should be_installed to test apache2'

 describe package('apache2') do
   it { should be_installed }
 end
end

control 'apache2 Configuration File' do
 impact 1.0
 title 'Check if mysql is installed'
 desc 'test to chels'

 describe file("/etc/apache2/apache2.conf") do
   it {should be_file}
 end
end

control 'apache2-Version' do
 impact 1.0
 title 'apache2-version'
 desc 'test for checking apache2 version'

 describe package('apache2') do
   its('version') { should cmp >= '*2.4.52*'}
 end
end

control 'apache2 is running' do
 impact 1.0
 title 'Check if apache2 is running'
 desc 'Test if the apache2 service is running'

 describe service('apache2') do
  it { should be_enabled }
  it { should be_running }
 end

 describe port(80) do
  it { should be_listening }
 end

end

control 'apache2 is running (test without systemctl)' do
  impact 1.0
  title 'Check if apache2 is running using "service" command'
  desc 'Test if the apache2 service is running'

  describe command ('service apache2 status') do
    its ('exit_status') {should eq 0}
 end
end