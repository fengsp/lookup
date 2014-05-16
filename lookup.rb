require 'formula'

class Lookup < Formula
  homepage 'https://github.com/fengsp/lookup/'
  url 'http://pypi.python.org/packages/source/h/lookup/lookup-0.1.tar.gz'

  def install
    setup_args = ['setup.py', 'install']
    system "python", *setup_args
  end

  def scripts_folder
    HOMEBREW_PREFIX/"share/python"
  end

  def caveats
    <<-EOS.undent
      To run the `lookup` command, you'll need to add Python's script directory to your PATH:
        #{scripts_folder}
    EOS
  end
end
