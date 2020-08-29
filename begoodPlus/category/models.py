from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify
class Category(models.Model):
       
    #slug = models.SlugField(_(u'slug'), max_length=100, unique=True)
    title = models.CharField(_(u'title'), max_length=250)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child', on_delete=models.CASCADE)
    itemsCount = models.IntegerField(default=0)
    catalog_rep = models.CharField(verbose_name=_('catalog representation'),max_length=1, blank=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['-title']
    
    def __str__(self):
        p_list = self._recurse_for_parents(self)
        p_list.append(self.title)
        return self.get_separator().join(p_list)
    
    def _recurse_for_parents(self, cat_obj):
        p_list = []
        if cat_obj.parent_id:
            p = cat_obj.parent
            p_list.append(p.title)
            more = self._recurse_for_parents(p)
            p_list.extend(more)
        if cat_obj == self and p_list:
            p_list.reverse()
        return p_list
    
    def get_separator(self):
        return ' :: '
    
    def _parents_repr(self):
        p_list = self._recurse_for_parents(self)
        return self.get_separator().join(p_list)
    _parents_repr.short_description = 'Category parents'
    
    def save(self):
        p_list = self._recurse_for_parents(self)
        if self.title in p_list:
            raise validators.ValidationError('You must not save a category in itself')
        super(Category, self).save()
    
    #@models.per
    def get_absolute_url(self):
        ret = ('category_index', (), { 'category': self.title })
        print('get_absolute_url', ret)
        return ret

# Create your models here.
#class Category(models.Model):
#    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.SET_NULL)
#    name = models.CharField(max_length=50)

    #def __str__(self):
        #ret = ''
        #if self.parent != None:
            #ret += self.parent.__str__() + ' > '
        #ret += self.name
        #return ret

