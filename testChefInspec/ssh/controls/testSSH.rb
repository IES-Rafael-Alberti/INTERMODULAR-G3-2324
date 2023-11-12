title "Test SSH"


control 'SSH Installation' do
 impact 1.0
 title 'Check if SSH is installed with be_installed'
 desc 'Use should be_installed to test ssh'

 describe package('ssh') do
   it { should be_installed }
 end
end

control 'SSH Configuration File' do
 impact 1.0
 title 'Check if SSH is installed'
 desc 'test to chels'

 describe file("/etc/ssh/ssh_config") do
   it {should be_file}
 end
end

control 'ssh-Version' do
 impact 1.0
 title 'ssh-version'
 desc 'test for checking ssh version'

 describe package('ssh') do
   its('version') { 
    should cmp >= '*8.2p1*'
  }
 end
end

control 'SSH is running' do
 impact 1.0
 title 'Check if SSH is running'
 desc 'Test if the SSH service is running'

 describe service('ssh') do
  it { should be_enabled }
  it { should be_running }
 end

 describe port(22) do
  it { should be_listening }
 end
end

control 'SSH is running (test without systemctl)' do
  impact 1.0
  title 'Check if SSH is running using "service" command'
  desc 'Test if the SSH service is running'

  describe command ('service ssh status') do
    its ('exit_status') {should eq 0}
 end
end
