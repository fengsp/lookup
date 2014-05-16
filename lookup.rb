require 'formula'

class Lookup < Formula
  homepage 'https://github.com/fengsp/lookup/'
  url 'https://pypi.python.org/packages/source/l/lookup/lookup-0.1.tar.gz'
  sha1 '080fb5a7664c6ada28db83be62820201fb434d84'

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
