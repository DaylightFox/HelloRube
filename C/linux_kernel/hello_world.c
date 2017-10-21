#include <linux/module.h>
#include <linux/init.h>
#include <linux/kernel.h>

#include <linux/fs.h>
#include <linux/proc_fs.h>
#include <linux/seq_file.h>

#define procfs_msg "Hello World\n"
#define procfs_name "hello_world"
#define procfs_parent NULL
#define procfs_perms 0644

static struct proc_dir_entry *procfs_hw_file;

static int
procfs_hw_show (struct seq_file *m, void *v)
{
  seq_printf (m, "%s\n", procfs_msg);

  return 0;
}

static int
procfs_hw_open (struct inode *inode, struct file *file)
{
  return single_open (file, procfs_hw_show, NULL);
}

static const struct file_operations procfs_hw_fops = {
  .owner = THIS_MODULE,
  .open = procfs_hw_open,
  .read = seq_read,
  .llseek = seq_lseek,
  .release = single_release,
};

static int __init
procfs_hw_init (void)
{
  procfs_hw_file =
    proc_create (procfs_name, procfs_perms, procfs_parent, &procfs_hw_fops);

  if (!procfs_hw_file)
    {
      return -ENOMEM;
    }

  return 0;
}

static void __exit
procfs_hw_exit (void)
{
  remove_proc_entry ("procfs_hw", procfs_parent);
}

module_init (procfs_hw_init);
module_exit (procfs_hw_exit);

MODULE_LICENSE ("GPL");
MODULE_AUTHOR ("d-grossman");
MODULE_DESCRIPTION ("procfs hello world");
